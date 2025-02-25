# import fitz  # PyMuPDF
# import json
# from pathlib import Path
# from langchain.tools import tool
# import textwrap
# import logging
# from typing import Dict, Any

# class PDFTools:
#     """PDF processing tools for use with CrewAI agents"""

#     def __init__(self):
#         # Setup logging
#         logging.basicConfig(level=logging.INFO)
#         self.logger = logging.getLogger(__name__)

#     @tool("Extract text content from PDF")
#     def extract_text_from_pdf(self, pdf_path: str) -> str:
#         """
#         Extract text from a PDF file.
        
#         Args:
#             pdf_path (str): Path to the PDF file to process
            
#         Returns:
#             str: JSON string containing the status and extracted text from each page
#         """
#         try:
#             doc = fitz.open(pdf_path)
            
#             # Extract text from each page
#             text_content = {}
#             for page_num, page in enumerate(doc):
#                 text_content[page_num] = page.get_text()
            
#             doc.close()

#             result = {
#                 "status": "success",
#                 "data": text_content,
#                 "metadata": {
#                     "total_pages": len(text_content),
#                     "file_name": Path(pdf_path).name
#                 },
#                 "summary": self._generate_summary(text_content)
#             }

#         except Exception as e:
#             self.logger.error(f"Error extracting text: {e}")
#             result = {
#                 "status": "error",
#                 "message": f"Failed to extract text: {str(e)}"
#             }

#         return json.dumps(result, indent=2)

#     @tool("Index extracted PDF content")
#     def index_text(self, texts: Dict[int, str]) -> str:
#         """
#         Index the extracted text content by page numbers.
        
#         Args:
#             texts (dict): Dictionary of extracted text from each page
            
#         Returns:
#             str: JSON string containing indexed content
#         """
#         try:
#             indexed_content = {
#                 page_num: {
#                     "content": content,
#                     "length": len(content),
#                     "summary": textwrap.shorten(content, width=200, placeholder="...")
#                 }
#                 for page_num, content in texts.items()
#             }

#             result = {
#                 "status": "success",
#                 "data": indexed_content
#             }

#         except Exception as e:
#             self.logger.error(f"Error indexing text: {e}")
#             result = {
#                 "status": "error",
#                 "message": f"Failed to index text: {str(e)}"
#             }

#         return json.dumps(result, indent=2)

#     @tool("Extract and index PDF content")
#     def extract_and_index(self, pdf_path: str) -> str:
#         """
#         Extract text from PDF and create indexed content.
        
#         Args:
#             pdf_path (str): Path to the PDF file
            
#         Returns:
#             str: JSON string containing indexed content with page numbers
#         """
#         # Extract text first
#         extraction_result = json.loads(self.extract_text_from_pdf(pdf_path))
        
#         if extraction_result["status"] == "success":
#             # Then index the extracted text
#             return self.index_text(extraction_result["data"])
#         else:
#             return json.dumps(extraction_result)

#     def _generate_summary(self, text_content: Dict[int, str]) -> Dict[str, Any]:
#         """
#         Generate a summary of the extracted text.
        
#         Args:
#             text_content (dict): Dictionary of extracted text from each page
            
#         Returns:
#             dict: Summary information about the content
#         """
#         try:
#             # Generate page previews
#             previews = {
#                 page_num: textwrap.shorten(content, width=200, placeholder="...")
#                 for page_num, content in text_content.items()
#             }

#             # Calculate basic statistics
#             total_chars = sum(len(text) for text in text_content.values())
#             total_words = sum(len(text.split()) for text in text_content.values())

#             return {
#                 "total_pages": len(text_content),
#                 "total_characters": total_chars,
#                 "total_words": total_words,
#                 "page_previews": previews
#             }

#         except Exception as e:
#             self.logger.error(f"Error generating summary: {e}")
#             return {
#                 "error": str(e)
#             }










import fitz  # PyMuPDF
import json
from langchain.tools import tool
import textwrap
from pathlib import Path

from typing import Dict, Any
from typing_extensions import TypeAlias  # For Python < 3.10

#Document: TypeAlias = fitz.Document
Document: TypeAlias = Any

class PDFExtractionTools:

    @tool("Extract unstructured data from PDF and index them for use.")
    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """
        Extract text from the provided PDF file.

        Args:
            pdf_path (str): Path to the PDF file from which text needs to be extracted.

        Returns:
            str: JSON string containing the status and extracted text from each page of the PDF.
        """
        try:
            # Explicitly annotate the document variable
            #doc: Document = fitz.open(pdf_path)
            doc: Any = fitz.open(pdf_path)

            
            # Now doc is properly typed
            text: Dict[int, str] = {
                page_num: page.get_text() 
                for page_num, page in enumerate(doc)
            }
            
            # Make sure to close the document
            doc.close()
            
            result: Dict[str, Any] = {
                "status": "success", 
                "data": text, 
                "summary": self._generate_summary(text)
            }
            
        except Exception as e:
            result = {
                "status": "error", 
                "message": f"An error occurred while extracting text: {str(e)}"
            }
        
        return json.dumps(result, indent=2)

    @tool("Index text extracted from PDF.")
    def index_text(self, texts: Dict[int, str]) -> str:
        """
        Index the extracted text.

        Args:
            texts (dict): Dictionary of extracted text from each page of the PDF.

        Returns:
            str: JSON string containing the status and indexed text with page numbers as keys.
        """
        try:
            # Here we return the same text, as it is already indexed by page numbers
            result = {"status": "success", "data": texts}
        except Exception as e:
            result = {"status": "error", "message": f"An error occurred while indexing text: {str(e)}"}
        
        return json.dumps(result, indent=2)

    @tool("Extract text from PDF and index it.")
    def extract_and_index(self, pdf_path: str) -> str:
        """
        Extract text from the PDF file and index it.

        Args:
            pdf_path (str): Path to the PDF file.

        Returns:
            str: JSON string containing the status and indexed text with page numbers as keys.
        """
        extraction_result = self.extract_text_from_pdf(pdf_path)
        extraction_result_dict = json.loads(extraction_result)

        if extraction_result_dict["status"] == "success":
            indexing_result = self.index_text(extraction_result_dict["data"])
            return indexing_result
        else:
            return extraction_result

    def _generate_summary(self, text: Dict[int, str]) -> Dict[str, Any]:
        """
        Generate a summary of the extracted text.

        Args:
            text (dict): Dictionary of extracted text from each page of the PDF.

        Returns:
            dict: Summary of the text including the number of pages and an overview of content.
        """
        num_pages = len(text)
        preview_texts = {
            page_num: content[:200] + '...' 
            for page_num, content in text.items()
        }
        return {
            "total_pages": num_pages,
            "page_previews": preview_texts
        }
