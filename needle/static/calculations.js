$(document).ready(function()
{
  var val1 = document.getElementById('calc1')

  if (val1 > 50) {
      document.getElementById('calc1').style.color = rgb(0,256,0)
  } else {
    document.getElementById('calc1').style.color = rgb(256,0,0)
  }

}
)
