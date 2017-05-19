#version 330 core

in vec2 uv;

void main(void) {
    vec4 outputColor = vec4( uv.x,uv.y,uv.x*uv.y,1.0);
    gl_FragColor = outputColor;
}
