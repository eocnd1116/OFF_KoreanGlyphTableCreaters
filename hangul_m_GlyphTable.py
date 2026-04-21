text = """
   [{}]
    0 Glyph data
     0 unsigned int m_Index = {}
     0 GlyphMetrics m_Metrics
      0 float m_Width = {}
      0 float m_Height = {}
      0 float m_HorizontalBearingX = 0
      0 float m_HorizontalBearingY = 9
      0 float m_HorizontalAdvance = 10
     0 GlyphRect m_GlyphRect
      0 int m_X = {}
      0 int m_Y = {}
      0 int m_Width = {}
      0 int m_Height = {}
     0 float m_Scale = 1
     0 int m_AtlasIndex = 0
     0 int m_ClassDefinitionType = 0"""
endtext = """
   [2523]
    0 Glyph data
     0 unsigned int m_Index = 2524
     0 GlyphMetrics m_Metrics
      0 float m_Width = 9
      0 float m_Height = 9
      0 float m_HorizontalBearingX = 0
      0 float m_HorizontalBearingY = 9
      0 float m_HorizontalAdvance = 10
     0 GlyphRect m_GlyphRect
      0 int m_X = 712
      0 int m_Y = 2
      0 int m_Width = 9
      0 int m_Height = 9
     0 float m_Scale = 1
     0 int m_AtlasIndex = 0
     0 int m_ClassDefinitionType = 0
   [2524]
    0 Glyph data
     0 unsigned int m_Index = 2525
     0 GlyphMetrics m_Metrics
      0 float m_Width = 9
      0 float m_Height = 9
      0 float m_HorizontalBearingX = 0
      0 float m_HorizontalBearingY = 9
      0 float m_HorizontalAdvance = 10
     0 GlyphRect m_GlyphRect
      0 int m_X = 723
      0 int m_Y = 2
      0 int m_Width = 9
      0 int m_Height = 9
     0 float m_Scale = 1
     0 int m_AtlasIndex = 0
     0 int m_ClassDefinitionType = 0
   [2525]
    0 Glyph data
     0 unsigned int m_Index = 2526
     0 GlyphMetrics m_Metrics
      0 float m_Width = 9
      0 float m_Height = 9
      0 float m_HorizontalBearingX = 0
      0 float m_HorizontalBearingY = 9
      0 float m_HorizontalAdvance = 10
     0 GlyphRect m_GlyphRect
      0 int m_X = 734
      0 int m_Y = 2
      0 int m_Width = 9
      0 int m_Height = 9
     0 float m_Scale = 1
     0 int m_AtlasIndex = 0
     0 int m_ClassDefinitionType = 0
   [2526]
    0 Glyph data
     0 unsigned int m_Index = 2527
     0 GlyphMetrics m_Metrics
      0 float m_Width = 9
      0 float m_Height = 9
      0 float m_HorizontalBearingX = 0
      0 float m_HorizontalBearingY = 9
      0 float m_HorizontalAdvance = 10
     0 GlyphRect m_GlyphRect
      0 int m_X = 745
      0 int m_Y = 2
      0 int m_Width = 9
      0 int m_Height = 9
     0 float m_Scale = 1
     0 int m_AtlasIndex = 0
     0 int m_ClassDefinitionType = 0"""

for i in range(1, 2351-4):
    print(text.format(176+i,177+i,9,9,151+11*((i-1)%51),497-11*((i-1)//51),9,9),end="")
print(endtext)
