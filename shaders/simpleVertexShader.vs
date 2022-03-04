in vec3 position;
uniform mat4 projectionMatrix; 
uniform mat4 modelMatrix;
in vec3 vertexColor;
out vec3 color; 

void main(){
    gl_Position = projectionMatrix *
    modelMatrix * vec4(position, 1.0); 
    color = vertexColor;
}