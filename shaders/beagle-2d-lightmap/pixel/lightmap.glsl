#version 330 core

in vec2 uv;
uniform vec2 position;

float RayToLineSegment(float x, float y, float dx, float dy, float x1, float y1, float x2, float y2)
{
    float r;
    float s;
    float d;

    if (dy / dx != (y2 - y1) / (x2 - x1))
    {
        d = ((dx * (y2 - y1)) - dy * (x2 - x1));
        if (d != 0)
        {
            r = (((y - y1) * (x2 - x1)) - (x - x1) * (y2 - y1)) / d;
            s = (((y - y1) * dx) - (x - x1) * dy) / d;
            if (r >= 0 && s >= 0 && s <= 1)
            {
                return length( vec2( dx,dy) ) * r;
                //return { x: x + r * dx, y: y + r * dy };
            }
        }
    }
    return 100000000.0;
}

void main(void) {
    vec2 mod_uv = (uv*2)-vec2(1.0,1.0);

    vec2 position = position * 0.5;
    vec2 line_a = vec2(-0.2,-0.4);
    vec2 line_b = vec2(0.2,0.1);

    float dist_to_position = 1.0 - distance( position, mod_uv );

    float intersection_distance = RayToLineSegment( position.x, position.y, mod_uv.x - position.x, mod_uv.y - position.y, line_a.x, line_a.y, line_b.x, line_b.y);

    float sees_player = 0.0;
    if( intersection_distance < dist_to_position ) {
        sees_player = 1.0;
    } 

    vec4 outputColor = vec4( intersection_distance, intersection_distance, sees_player, 1.0); 
    gl_FragColor = outputColor;
}
