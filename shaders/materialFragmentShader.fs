uniform vec3 baseColor; 
uniform bool useVertexColors; 
in vec3 color; 
out vec4 fragColor;
void main() { 
    fragColor = vec4(baseColor, 1.0);
    if ( useVertexColors ){ 
        fragColor = vec4(color, 1.0);
    }
} 