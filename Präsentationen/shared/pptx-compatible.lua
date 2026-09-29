-- Keep native editable text, avoiding Quarto callout shape-ID collisions in PPTX.
function Meta(meta)
  -- HSM title layout has no date placeholder. Pandoc otherwise writes an empty p:sp.
  if FORMAT == 'pptx' then meta.date = nil end
  return meta
end
function Div(el)
  if FORMAT ~= 'pptx' then return nil end
  for _, class in ipairs(el.classes) do
    if class:match('^callout%-') then
      local blocks = pandoc.Blocks{}
      if el.attributes.title then
        blocks:insert(pandoc.Para{pandoc.Strong{pandoc.Str(el.attributes.title)}})
      end
      blocks:extend(el.content)
      return blocks
    end
  end
end
function Callout(el)
  if FORMAT ~= 'pptx' then return nil end
  local blocks = pandoc.Blocks{}
  if el.title then blocks:insert(pandoc.Para{pandoc.Strong{pandoc.Str(pandoc.utils.stringify(el.title))}}) end
  if pandoc.utils.type(el.content) == 'Block' then
    if el.content.t == 'Div' then blocks:extend(el.content.content) else blocks:insert(el.content) end
  else blocks:extend(el.content) end
  return pandoc.Div(blocks)
end
