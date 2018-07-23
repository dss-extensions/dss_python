from ._utils import *

def Reset():
    lib.RegControls_Reset()
    return 0

def AllNames():
    '''(read-only) Array of strings containing all RegControl names'''
    return get_string_array(lib.RegControls_Get_AllNames)

def CTPrimary(*args):
    '''CT primary ampere rating (secondary is 0.2 amperes)'''
    # Getter
    if len(args) == 0:
        return lib.RegControls_Get_CTPrimary()
    
    # Setter
    Value, = args
    lib.RegControls_Set_CTPrimary(Value)

def Count():
    '''(read-only) Number of RegControl objects in Active Circuit'''
    return lib.RegControls_Get_Count()

def Delay(*args):
    '''Time delay [s] after arming before the first tap change. Control may reset before actually changing taps.'''
    # Getter
    if len(args) == 0:
        return lib.RegControls_Get_Delay()
    
    # Setter
    Value, = args
    lib.RegControls_Set_Delay(Value)

def First():
    '''(read-only) Sets the first RegControl active. Returns 0 if none.'''
    return lib.RegControls_Get_First()

def ForwardBand(*args):
    '''Regulation bandwidth in forward direciton, centered on Vreg'''
    # Getter
    if len(args) == 0:
        return lib.RegControls_Get_ForwardBand()
    
    # Setter
    Value, = args
    lib.RegControls_Set_ForwardBand(Value)

def ForwardR(*args):
    '''LDC R setting in Volts'''
    # Getter
    if len(args) == 0:
        return lib.RegControls_Get_ForwardR()
    
    # Setter
    Value, = args
    lib.RegControls_Set_ForwardR(Value)

def ForwardVreg(*args):
    '''Target voltage in the forward direction, on PT secondary base.'''
    # Getter
    if len(args) == 0:
        return lib.RegControls_Get_ForwardVreg()
    
    # Setter
    Value, = args
    lib.RegControls_Set_ForwardVreg(Value)

def ForwardX(*args):
    '''LDC X setting in Volts'''
    # Getter
    if len(args) == 0:
        return lib.RegControls_Get_ForwardX()
    
    # Setter
    Value, = args
    lib.RegControls_Set_ForwardX(Value)

def IsInverseTime(*args):
    '''Time delay is inversely adjsuted, proportinal to the amount of voltage outside the regulating band.'''
    # Getter
    if len(args) == 0:
        return 1 if lib.RegControls_Get_IsInverseTime() else 0
    
    # Setter
    Value, = args
    lib.RegControls_Set_IsInverseTime(Value)

def IsReversible(*args):
    '''Regulator can use different settings in the reverse direction.  Usually not applicable to substation transformers.'''
    # Getter
    if len(args) == 0:
        return 1 if lib.RegControls_Get_IsReversible() else 0
    
    # Setter
    Value, = args
    lib.RegControls_Set_IsReversible(Value)

def MaxTapChange(*args):
    '''Maximum tap change per iteration in STATIC solution mode. 1 is more realistic, 16 is the default for a faster soluiton.'''
    # Getter
    if len(args) == 0:
        return lib.RegControls_Get_MaxTapChange()
    
    # Setter
    Value, = args
    lib.RegControls_Set_MaxTapChange(Value)

def MonitoredBus(*args):
    '''Name of a remote regulated bus, in lieu of LDC settings'''
    # Getter
    if len(args) == 0:
        return get_string(lib.RegControls_Get_MonitoredBus())
    
    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.RegControls_Set_MonitoredBus(Value)
    return '0'

def Name(*args):
    '''
    (read) Get/set Active RegControl  name
    (write) Sets a RegControl active by name
    '''
    # Getter
    if len(args) == 0:
        return get_string(lib.RegControls_Get_Name())
    
    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.RegControls_Set_Name(Value)
    return '0'

def Next():
    '''(read-only) Sets the next RegControl active. Returns 0 if none.'''
    return lib.RegControls_Get_Next()

def PTRatio(*args):
    '''PT ratio for voltage control settings'''
    # Getter
    if len(args) == 0:
        return lib.RegControls_Get_PTratio()
    
    # Setter
    Value, = args
    lib.RegControls_Set_PTratio(Value)

def ReverseBand(*args):
    '''Bandwidth in reverse direction, centered on reverse Vreg.'''
    # Getter
    if len(args) == 0:
        return lib.RegControls_Get_ReverseBand()
    
    # Setter
    Value, = args
    lib.RegControls_Set_ReverseBand(Value)

def ReverseR(*args):
    '''Reverse LDC R setting in Volts.'''
    # Getter
    if len(args) == 0:
        return lib.RegControls_Get_ReverseR()
    
    # Setter
    Value, = args
    lib.RegControls_Set_ReverseR(Value)

def ReverseVreg(*args):
    '''Target voltage in the revese direction, on PT secondary base.'''
    # Getter
    if len(args) == 0:
        return lib.RegControls_Get_ReverseVreg()
    
    # Setter
    Value, = args
    lib.RegControls_Set_ReverseVreg(Value)

def ReverseX(*args):
    '''Reverse LDC X setting in volts.'''
    # Getter
    if len(args) == 0:
        return lib.RegControls_Get_ReverseX()
    
    # Setter
    Value, = args
    lib.RegControls_Set_ReverseX(Value)

def TapDelay(*args):
    '''Time delay [s] for subsequent tap changes in a set. Control may reset before actually changing taps.'''
    # Getter
    if len(args) == 0:
        return lib.RegControls_Get_TapDelay()
    
    # Setter
    Value, = args
    lib.RegControls_Set_TapDelay(Value)

def TapNumber(*args):
    '''Integer number of the tap that the controlled transformer winding is currentliy on.'''
    # Getter
    if len(args) == 0:
        return lib.RegControls_Get_TapNumber()
    
    # Setter
    Value, = args
    lib.RegControls_Set_TapNumber(Value)

def TapWinding(*args):
    '''Tapped winding number'''
    # Getter
    if len(args) == 0:
        return lib.RegControls_Get_TapWinding()
    
    # Setter
    Value, = args
    lib.RegControls_Set_TapWinding(Value)

def Transformer(*args):
    '''Name of the transformer this regulator controls'''
    # Getter
    if len(args) == 0:
        return get_string(lib.RegControls_Get_Transformer())
    
    # Setter
    Value, = args
    if type(Value) is not bytes:
        Value = Value.encode(codec)

    lib.RegControls_Set_Transformer(Value)
    return '0'

def VoltageLimit(*args):
    '''First house voltage limit on PT secondary base.  Setting to 0 disables this function.'''
    # Getter
    if len(args) == 0:
        return lib.RegControls_Get_VoltageLimit()
    
    # Setter
    Value, = args
    lib.RegControls_Set_VoltageLimit(Value)

def Winding(*args):
    '''Winding number for PT and CT connections'''
    # Getter
    if len(args) == 0:
        return lib.RegControls_Get_Winding()
    
    # Setter
    Value, = args
    lib.RegControls_Set_Winding(Value)



_columns = ['CTPrimary', 'Delay', 'ForwardBand', 'ForwardR', 'ForwardVreg', 'ForwardX', 'IsInverseTime', 'IsReversible', 'MaxTapChange', 'MonitoredBus', 'Name', 'PTRatio', 'ReverseBand', 'ReverseR', 'ReverseVreg', 'ReverseX', 'TapDelay', 'TapNumber', 'TapWinding', 'Transformer', 'VoltageLimit', 'Winding']
__all__ = ['Reset', 'AllNames', 'CTPrimary', 'Count', 'Delay', 'First', 'ForwardBand', 'ForwardR', 'ForwardVreg', 'ForwardX', 'IsInverseTime', 'IsReversible', 'MaxTapChange', 'MonitoredBus', 'Name', 'Next', 'PTRatio', 'ReverseBand', 'ReverseR', 'ReverseVreg', 'ReverseX', 'TapDelay', 'TapNumber', 'TapWinding', 'Transformer', 'VoltageLimit', 'Winding']

