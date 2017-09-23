inst=institution(self)
inst.ShowModal()
self.label_institution.SetForegroundColour(self.label_fg_color)
inst.Destroy()
event.Skip()

