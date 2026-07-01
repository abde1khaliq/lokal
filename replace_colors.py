import re

with open('components/VHome.tsx', 'r') as f:
    content = f.read()

# Replace PINS accentColors
content = re.sub(r'accentColor:\s*"hsl\([^)]+\)"', 'accentColor: "#4A3B2C"', content)

# Replace background gradients
content = content.replace(
    'bg="linear-gradient(160deg, hsl(240,15%,6%) 0%, hsl(260,20%,8%) 50%, hsl(230,15%,6%) 100%)"',
    'bg="#000000"'
)

# Ambient orbs
content = re.sub(
    r'bg="radial-gradient\(circle, hsla\([^)]+\) 0%, transparent 70%\)"',
    'bg="radial-gradient(circle, rgba(74, 59, 44, 0.15) 0%, transparent 70%)"',
    content
)

# Navbar
content = content.replace('bg="hsla(240,15%,8%,0.55)"', 'bg="rgba(0, 0, 0, 0.55)"')
content = content.replace('borderBottom="1px solid hsla(260,40%,60%,0.12)"', 'borderBottom="1px solid rgba(255, 255, 255, 0.1)"')

# Search bar
content = content.replace('bg="hsla(260,15%,15%,0.6)"', 'bg="rgba(255, 255, 255, 0.05)"')
content = content.replace('border="1px solid hsla(260,30%,50%,0.15)"', 'border="1px solid rgba(255, 255, 255, 0.1)"')
content = content.replace('_hover={{\n            bg: "hsla(260,15%,18%,0.7)",\n            borderColor: "hsla(260,40%,60%,0.3)",\n            boxShadow: "0 0 20px hsla(260,60%,50%,0.1)",\n          }}',
                          '_hover={{\n            bg: "rgba(255, 255, 255, 0.1)",\n            borderColor: "#4A3B2C",\n            boxShadow: "0 0 20px rgba(74, 59, 44, 0.2)",\n          }}')
content = content.replace('color="hsla(260,30%,70%,0.6)"', 'color="rgba(255, 255, 255, 0.6)"')
content = content.replace('_placeholder={{ color: "hsla(260,20%,60%,0.5)" }}', '_placeholder={{ color: "rgba(255, 255, 255, 0.5)" }}')

# Right side icons
content = content.replace('bg="linear-gradient(135deg, hsl(270,80%,60%), hsl(200,90%,55%))"', 'bg="#4A3B2C"')
content = content.replace('boxShadow="0 0 16px hsla(270,80%,60%,0.5)"', 'boxShadow="0 0 16px rgba(74, 59, 44, 0.5)"')
content = content.replace('"--avatar-bg": "hsl(260,20%,18%)"', '"--avatar-bg": "rgba(255, 255, 255, 0.1)"')

# Sidebar
content = content.replace('bg="hsla(240,15%,8%,0.45)"', 'bg="rgba(0, 0, 0, 0.45)"')
content = content.replace('borderRight="1px solid hsla(260,40%,60%,0.08)"', 'borderRight="1px solid rgba(255, 255, 255, 0.1)"')

# Profile card
content = content.replace('bg="hsla(260,15%,14%,0.5)"', 'bg="rgba(255, 255, 255, 0.05)"')
content = content.replace('border="1px solid hsla(260,30%,50%,0.1)"', 'border="1px solid rgba(255, 255, 255, 0.1)"')
content = content.replace('_hover={{\n                bg: "hsla(260,15%,18%,0.6)",\n                borderColor: "hsla(260,40%,60%,0.2)",\n              }}',
                          '_hover={{\n                bg: "rgba(255, 255, 255, 0.1)",\n                borderColor: "rgba(255, 255, 255, 0.2)",\n              }}')
content = content.replace('"--avatar-bg": "hsl(270,60%,40%)"', '"--avatar-bg": "#4A3B2C"')
content = content.replace('color="hsla(260,20%,60%,0.7)"', 'color="rgba(255, 255, 255, 0.7)"')
content = content.replace('color="hsla(260,20%,60%,0.5)"', 'color="rgba(255, 255, 255, 0.5)"')

# NavLink
content = content.replace('bg={active ? "hsla(260,60%,50%,0.15)" : "transparent"}', 'bg={active ? "rgba(74, 59, 44, 0.2)" : "transparent"}')
content = content.replace('color={active ? "hsl(270,80%,80%)" : "hsla(260,20%,70%,0.7)"}', 'color={active ? "#4A3B2C" : "rgba(255, 255, 255, 0.7)"}')
content = content.replace('_hover={{\n        bg: active\n          ? "hsla(260,60%,50%,0.2)"\n          : "hsla(260,20%,30%,0.3)",\n        color: "white",\n      }}',
                          '_hover={{\n        bg: active\n          ? "rgba(74, 59, 44, 0.3)"\n          : "rgba(255, 255, 255, 0.1)",\n        color: "white",\n      }}')

# GlassIconButton
content = content.replace('color="hsla(260,20%,70%,0.7)"', 'color="rgba(255, 255, 255, 0.7)"')
content = content.replace('_hover={{\n          bg: "hsla(260,20%,30%,0.4)",\n          color: "white",\n        }}',
                          '_hover={{\n          bg: "rgba(255, 255, 255, 0.1)",\n          color: "white",\n        }}')
content = content.replace('bg="hsl(0,90%,60%)"', 'bg="#4A3B2C"')
content = content.replace('boxShadow="0 0 8px hsla(0,90%,60%,0.6)"', 'boxShadow="0 0 8px rgba(74, 59, 44, 0.6)"')

# SidebarItem
content = content.replace('bg={active ? "hsla(260,50%,50%,0.12)" : "transparent"}', 'bg={active ? "rgba(74, 59, 44, 0.2)" : "transparent"}')
content = content.replace('color={active ? "hsl(270,80%,80%)" : "hsla(260,20%,60%,0.7)"}', 'color={active ? "white" : "rgba(255, 255, 255, 0.7)"}')
content = content.replace('_hover={{\n        bg: active\n          ? "hsla(260,50%,50%,0.18)"\n          : "hsla(260,20%,25%,0.35)",\n        color: "white",\n      }}',
                          '_hover={{\n        bg: active\n          ? "rgba(74, 59, 44, 0.3)"\n          : "rgba(255, 255, 255, 0.1)",\n        color: "white",\n      }}')
content = content.replace('bg="linear-gradient(180deg, hsl(270,80%,60%), hsl(200,90%,55%))"', 'bg="#4A3B2C"')
content = content.replace('boxShadow="0 0 8px hsla(270,80%,60%,0.5)"', 'boxShadow="0 0 8px rgba(74, 59, 44, 0.5)"')
content = content.replace('bg="hsla(340,80%,55%,0.2)"', 'bg="rgba(74, 59, 44, 0.2)"')
content = content.replace('color="hsl(340,80%,70%)"', 'color="#4A3B2C"')

# CategoryChip
content = content.replace('bg={\n        active\n          ? "linear-gradient(135deg, hsla(270,80%,60%,0.3), hsla(200,90%,55%,0.3))"\n          : "hsla(260,15%,14%,0.5)"\n      }',
                          'bg={\n        active\n          ? "#4A3B2C"\n          : "rgba(255, 255, 255, 0.05)"\n      }')
content = content.replace('border={\n        active\n          ? "1px solid hsla(270,60%,60%,0.35)"\n          : "1px solid hsla(260,30%,50%,0.1)"\n      }',
                          'border={\n        active\n          ? "1px solid #4A3B2C"\n          : "1px solid rgba(255, 255, 255, 0.1)"\n      }')
content = content.replace('color={active ? "hsl(270,80%,85%)" : "hsla(260,20%,65%,0.8)"}', 'color={active ? "white" : "rgba(255, 255, 255, 0.8)"}')
content = content.replace('boxShadow={active ? "0 0 16px hsla(270,60%,50%,0.15)" : "none"}', 'boxShadow={active ? "0 0 16px rgba(74, 59, 44, 0.3)" : "none"}')
content = content.replace('_hover={{\n        bg: active\n          ? "linear-gradient(135deg, hsla(270,80%,60%,0.4), hsla(200,90%,55%,0.4))"\n          : "hsla(260,15%,18%,0.6)",\n        borderColor: "hsla(260,40%,60%,0.25)",\n        color: "white",\n        transform: "translateY(-1px)",\n      }}',
                          '_hover={{\n        bg: active\n          ? "rgba(74, 59, 44, 0.8)"\n          : "rgba(255, 255, 255, 0.1)",\n        borderColor: active ? "#4A3B2C" : "rgba(255, 255, 255, 0.2)",\n        color: "white",\n        transform: "translateY(-1px)",\n      }}')

# PinCard
content = content.replace('bg="hsla(260,15%,12%,0.6)"', 'bg="rgba(255, 255, 255, 0.05)"')
content = content.replace('border="1px solid hsla(260,30%,50%,0.08)"', 'border="1px solid rgba(255, 255, 255, 0.1)"')
content = content.replace('boxShadow: `0 20px 60px hsla(260,50%,10%,0.5), 0 0 30px ${pin.accentColor}22`', 'boxShadow: `0 20px 60px rgba(0,0,0,0.5), 0 0 30px ${pin.accentColor}22`')

# PinCard saves and heart icon
content = content.replace('color="hsla(0,80%,65%,0.7)"', 'color="#4A3B2C"')
content = content.replace('color="hsla(260,20%,60%,0.6)"', 'color="rgba(255, 255, 255, 0.6)"')

# TrendingItem
content = content.replace('bg="hsla(260,15%,12%,0.4)"', 'bg="rgba(255, 255, 255, 0.05)"')
content = content.replace('border="1px solid hsla(260,30%,50%,0.06)"', 'border="1px solid rgba(255, 255, 255, 0.1)"')
content = content.replace('_hover={{\n        bg: "hsla(260,15%,16%,0.5)",\n        borderColor: `${color}33`,\n        boxShadow: `0 0 16px ${color}11`,\n        transform: "translateX(2px)",\n      }}',
                          '_hover={{\n        bg: "rgba(255, 255, 255, 0.1)",\n        borderColor: `${color}33`,\n        boxShadow: `0 0 16px ${color}11`,\n        transform: "translateX(2px)",\n      }}')
content = content.replace('color="hsla(260,20%,60%,0.3)"', 'color="rgba(255, 255, 255, 0.3)"')

# CreatorCard
content = content.replace('_hover={{\n        bg: "hsla(260,15%,16%,0.4)",\n        transform: "translateX(2px)",\n      }}',
                          '_hover={{\n        bg: "rgba(255, 255, 255, 0.1)",\n        transform: "translateX(2px)",\n      }}')
content = content.replace('"--avatar-bg": "hsl(270,50%,35%)"', '"--avatar-bg": "#4A3B2C"')
content = content.replace('bg="hsla(260,50%,50%,0.15)"', 'bg="rgba(74, 59, 44, 0.2)"')
content = content.replace('color="hsl(270,80%,75%)"', 'color="white"')
content = content.replace('border="1px solid hsla(260,40%,60%,0.15)"', 'border="1px solid #4A3B2C"')
content = content.replace('_hover={{\n          bg: "hsla(260,50%,50%,0.25)",\n          borderColor: "hsla(260,50%,60%,0.3)",\n          boxShadow: "0 0 12px hsla(260,60%,50%,0.15)",\n        }}',
                          '_hover={{\n          bg: "rgba(74, 59, 44, 0.4)",\n          borderColor: "#4A3B2C",\n          boxShadow: "0 0 12px rgba(74, 59, 44, 0.3)",\n        }}')

with open('components/VHome.tsx', 'w') as f:
    f.write(content)
