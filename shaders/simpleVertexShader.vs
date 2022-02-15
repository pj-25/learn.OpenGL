in vec3 position;
in vec3 vertexColor;
out vec3 color;

uniform vec3 translation;

void main(){
    gl_Position = vec4(position+translation, 1.0);
    color = vertexColor;
}