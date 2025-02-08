from langchain.tools import tool
import os

class ThreeJSSceneGenerator:
    # Set the fixed output path
    default_output_path = r'C:\Users\PC\Desktop\taj\starter_template\tools\three.js'

    @tool("Generates a Three.js scene script and saves it to the specified output path.")
    def generate_scene_script(self):
        """
        Generates a Three.js scene script and saves it to the specified output path.
        """
        script_content = """
        // Initialize Three.js scene
        var scene = new THREE.Scene();
        var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

        var renderer = new THREE.WebGLRenderer();
        renderer.setSize(window.innerWidth, window.innerHeight);
        document.body.appendChild(renderer.domElement);

        // Create cube
        var geometry = new THREE.BoxGeometry();
        var material = new THREE.MeshBasicMaterial({ color: 0x00ff00 });
        var cube = new THREE.Mesh(geometry, material);
        scene.add(cube);

        // Position cube
        camera.position.z = 5;

        // Add light
        var light = new THREE.PointLight(0xffffff);
        light.position.set(10, 10, 10);
        scene.add(light);

        // Render loop
        function animate() {
            requestAnimationFrame(animate);
            cube.rotation.x += 0.01;
            cube.rotation.y += 0.01;
            renderer.render(scene, camera);
        }
        animate();
        """
        
        try:
            # Use the fixed output path
            with open(self.default_output_path, 'w') as file:
                file.write(script_content)
            print(f"Three.js scene script generated and saved to {self.default_output_path}")
        except IOError as e:
            print(f"An error occurred while saving the script: {e}")

        return self.default_output_path
