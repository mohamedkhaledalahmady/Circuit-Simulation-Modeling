function varargout = Project_v2(varargin)
% PROJECT_V2 MATLAB code for Project_v2.fig
%      PROJECT_V2, by itself, creates a new PROJECT_V2 or raises the existing
%      singleton*.
%
%      H = PROJECT_V2 returns the handle to a new PROJECT_V2 or the handle to
%      the existing singleton*.
%
%      PROJECT_V2('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in PROJECT_V2.M with the given input arguments.
%
%      PROJECT_V2('Property','Value',...) creates a new PROJECT_V2 or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before Project_v2_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to Project_v2_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help Project_v2

% Last Modified by GUIDE v2.5 22-Aug-2024 16:30:12

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @Project_v2_OpeningFcn, ...
                   'gui_OutputFcn',  @Project_v2_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before Project_v2 is made visible.
function Project_v2_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to Project_v2 (see VARARGIN)

% Choose default command line output for Project_v2
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes Project_v2 wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = Project_v2_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on selection change in popupmenu1.
function popupmenu1_Callback(hObject, eventdata, handles)
comp_sel_str  = get(handles.popupmenu1, 'string');
comp_sel_val  = get(handles.popupmenu1, 'value');
switch comp_sel_str{comp_sel_val}
    case {'VCVS', 'VCCS',  'CCVS', 'CCCS'}
        set(handles.edit4, 'enable', 'on');
        set(handles.edit5, 'enable', 'on');
    otherwise
        set(handles.edit4, 'enable', 'off');
        set(handles.edit5, 'enable', 'off');
end
        
% hObject    handle to popupmenu1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns popupmenu1 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from popupmenu1


% --- Executes during object creation, after setting all properties.
function popupmenu1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to popupmenu1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function start_point_Callback(hObject, eventdata, handles)
if isempty(str2num(get(handles.start_point, 'string')))
    set(handles.start_error, 'string', 'Please enter number');
else
    set(handles.start_error, 'string', '');
end
% hObject    handle to start_point (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of start_point as text
%        str2double(get(hObject,'String')) returns contents of start_point as a double


% --- Executes during object creation, after setting all properties.
function start_point_CreateFcn(hObject, eventdata, handles)
% hObject    handle to start_point (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function end_point_Callback(hObject, eventdata, handles)
if isempty(str2num(get(handles.end_point, 'string')))
    set(handles.end_error, 'string', 'Please enter number');
else
    set(handles.end_error, 'string', '');
end
% hObject    handle to end_point (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of end_point as text
%        str2double(get(hObject,'String')) returns contents of end_point as a double


% --- Executes during object creation, after setting all properties.
function end_point_CreateFcn(hObject, eventdata, handles)
% hObject    handle to end_point (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in pushbutton1.
global R_values V_values I_values C_values L_values R_start R_end V_start V_end I_start I_end C_start C_end L_start L_end R_index V_index I_index C_index L_index
global VCCS_value VCCS_p VCCS_q VCCS_k VCCS_l VCCS_index
global VCVS_value VCVS_p VCVS_q VCVS_k VCVS_l VCVS_index
global CCCS_value CCCS_p CCCS_q CCCS_k CCCS_l CCCS_index
global CCVS_value CCVS_p cCVS_q CCVS_k CCVS_l CCVS_index
R_index = 0;
V_index = 0;
I_index = 0;
C_index = 0;
L_index = 0;
VCCS_index = 0;
VCVS_index = 0;
CCCS_index = 0;
CCVS_index = 0;
function pushbutton1_Callback(hObject, eventdata, handles)
global R_values V_values I_values C_values L_values R_start R_end V_start V_end I_start I_end C_start C_end L_start L_end R_index V_index I_index C_index L_index
global VCCS_values VCCS_p VCCS_q VCCS_k VCCS_l VCCS_index
global VCVS_values VCVS_p VCVS_q VCVS_k VCVS_l VCVS_index
global CCCS_values CCCS_p CCCS_q CCCS_k CCCS_l CCCS_index
global CCVS_values CCVS_p CCVS_q CCVS_k CCVS_l CCVS_index

comp_sel_str  = get(handles.popupmenu1, 'string');
comp_sel_val  = get(handles.popupmenu1, 'value');
comp_value     = str2num(get(handles.comp_value, 'string')); 
comp_unit       = get(handles.listbox1, 'value');
switch comp_unit
    case 1
        % G
        comp_value = comp_value * 1e9;
    case 2
        % M
        comp_value = comp_value * 1e6;
    case 3
        % K
        comp_value = comp_value * 1e3;
    case 4
        % same
        comp_value = comp_value * 1;
    case 5
        % m
        comp_value = comp_value * 1e-3;
    case 6
        % u
        comp_value = comp_value * 1e-6;
    case 7
        % n
        comp_value = comp_value * 1e-9;
    case 8
        % p
        comp_value = comp_value * 1e-12;
    case 9
        % f
        comp_value = comp_value * 1e-15;
    otherwise 
        comp_value = comp_value * 1;
end

switch comp_sel_str{comp_sel_val}
    case 'R'
        R_index = R_index + 1;
        R_values(R_index)   = comp_value;
        R_start(R_index)    = str2num(get(handles.start_point, 'string'));
        R_end(R_index)      = str2num(get(handles.end_point, 'string'));
    case 'V'
        V_index = V_index + 1;
        V_values(V_index)   = comp_value;
        V_start(V_index)    = str2num(get(handles.start_point, 'string'));
        V_end(V_index)      = str2num(get(handles.end_point, 'string'));
    case 'I'
        I_index = I_index + 1;
        I_values(I_index)   = comp_value;
        I_start(I_index)    = str2num(get(handles.start_point, 'string'));
        I_end(I_index)      = str2num(get(handles.end_point, 'string'));
    case 'C'
        C_index = C_index + 1;
        C_values(C_index)   = comp_value;
        C_start(C_index)    = str2num(get(handles.start_point, 'string'));
        C_end(C_index)      = str2num(get(handles.end_point, 'string'));
     case 'L'
        L_index = L_index + 1;
        L_values(L_index)   = comp_value;
        L_start(L_index)    = str2num(get(handles.start_point, 'string'));
        L_end(L_index)      = str2num(get(handles.end_point, 'string')); 
      case 'VCCS'
        VCCS_index = VCCS_index + 1;
        VCCS_values(VCCS_index)   = comp_value;
        VCCS_p(VCCS_index)    = str2num(get(handles.start_point, 'string'));
        VCCS_q(VCCS_index)      = str2num(get(handles.end_point, 'string'));
        VCCS_k(VCCS_index)    = str2num(get(handles.edit4, 'string'));
        VCCS_l(VCCS_index)      = str2num(get(handles.edit5, 'string'));
      case 'CCCS'
        CCCS_index = CCCS_index + 1;
        CCCS_values(CCCS_index)   = comp_value;
        CCCS_p(CCCS_index)    = str2num(get(handles.start_point, 'string'));
        CCCS_q(CCCS_index)      = str2num(get(handles.end_point, 'string'));
        CCCS_k(CCCS_index)    = str2num(get(handles.edit4, 'string'));
        CCCS_l(CCCS_index)      = str2num(get(handles.edit5, 'string'));
      case 'VCVS'
        VCVS_index = VCVS_index + 1;
        VCVS_values(VCVS_index)   = comp_value;
        VCVS_p(VCVS_index)    = str2num(get(handles.start_point, 'string'));
        VCVS_q(VCVS_index)      = str2num(get(handles.end_point, 'string'));
        VCVS_k(VCVS_index)    = str2num(get(handles.edit4, 'string'));
        VCVS_l(VCVS_index)      = str2num(get(handles.edit5, 'string'));
     case 'CCVS'
        CCVS_index = CCVS_index + 1;
        CCVS_values(CCVS_index)   = comp_value;
        CCVS_p(CCVS_index)    = str2num(get(handles.start_point, 'string'));
        CCVS_q(CCVS_index)      = str2num(get(handles.end_point, 'string'));
        CCVS_k(CCVS_index)    = str2num(get(handles.edit4, 'string'));
        CCVS_l(CCVS_index)      = str2num(get(handles.edit5, 'string'));
end
% hObject    handle to pushbutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in pushbutton2.
function pushbutton2_Callback(hObject, eventdata, handles)
global R_values V_values I_values C_values L_values R_start R_end V_start V_end I_start I_end C_start C_end L_start L_end
global VCCS_values VCCS_p VCCS_q VCCS_k VCCS_l VCCS_index
global VCVS_values VCVS_p VCVS_q VCVS_k VCVS_l VCVS_index
global CCCS_values CCCS_p CCCS_q CCCS_k CCCS_l CCCS_index
global CCVS_values CCVS_p CCVS_q CCVS_k CCVS_l CCVS_index

file_d = fopen('Netlist.cir', 'w+t');
if file_d < 0
    error('Unable to open the file');
end
fprintf(file_d, '// Circuit Eample\n\n');
fprintf(file_d, '********** Voltage Sources ***********\n'); 
for ii = 1 : length(V_values)
    str = ['V' num2str(ii) ' ' num2str(V_start(ii)) ' ' num2str(V_end(ii)) ' ' num2str(V_values(ii))];
    fprintf(file_d, str);
    fprintf(file_d, '\n');
end
fprintf(file_d, '********** Current Sources **********\n'); 
for ii = 1 : length(I_values)
    str = ['I' num2str(ii) ' ' num2str(I_start(ii)) ' ' num2str(I_end(ii)) ' ' num2str(I_values(ii))];
    fprintf(file_d, str);
    fprintf(file_d, '\n');
end
fprintf(file_d, '********** Dependent Sources **********\n'); 
for ii = 1 : length(VCCS_values)
    str = ['G' num2str(ii) ' ' num2str(VCCS_p(ii)) ' ' num2str(VCCS_q(ii)) ' ' num2str(VCCS_k(ii)) ' ' num2str(VCCS_l(ii)) ' ' num2str(VCCS_values(ii))];
    fprintf(file_d, str);
    fprintf(file_d, '\n');
end
for ii = 1 : length(CCCS_values)
    % redundant voltage
    voltage_name = ['V' num2str(ii + length(V_values))];
    str = [voltage_name ' ' num2str(CCCS_k(ii)) ' ' num2str(CCCS_l(ii)) ' ' num2str(0)];
    fprintf(file_d, str);
    fprintf(file_d, '\n');
    
    str = ['F' num2str(ii) ' ' num2str(CCCS_p(ii)) ' ' num2str(CCCS_q(ii)) ' ' voltage_name ' ' num2str(CCCS_values(ii))];
    fprintf(file_d, str);
    fprintf(file_d, '\n');
end
for ii = 1 : length(VCVS_values)
    str = ['E' num2str(ii) ' ' num2str(VCVS_p(ii)) ' ' num2str(VCVS_q(ii)) ' ' num2str(VCVS_k(ii)) ' ' num2str(VCVS_l(ii)) ' ' num2str(VCVS_values(ii))];
    fprintf(file_d, str);
    fprintf(file_d, '\n');
end
for ii = 1 : length(CCVS_values)
    % redundant voltage
    voltage_name = ['V' num2str(ii + length(V_values) + length(CCCS_values))];
    str = [voltage_name ' ' num2str(CCVS_k(ii)) ' ' num2str(CCVS_l(ii)) ' ' num2str(0)];
    fprintf(file_d, str);
    fprintf(file_d, '\n');
    
    str = ['H' num2str(ii) ' ' num2str(CCVS_p(ii)) ' ' num2str(CCVS_q(ii)) ' ' voltage_name ' ' num2str(CCVS_values(ii))];
    fprintf(file_d, str);
    fprintf(file_d, '\n');
end

fprintf(file_d, '********** Resisitors **********\n'); 
for ii = 1 : length(R_values)
    str = ['R' num2str(ii) ' ' num2str(R_start(ii)) ' ' num2str(R_end(ii)) ' ' num2str(R_values(ii))];
    fprintf(file_d, str);
    fprintf(file_d, '\n');
end
fprintf(file_d, '********** Capacitors **********\n'); 
for ii = 1 : length(C_values)
    str = ['C' num2str(ii) ' ' num2str(C_start(ii)) ' ' num2str(C_end(ii)) ' ' num2str(C_values(ii))];
    fprintf(file_d, str);
    fprintf(file_d, '\n');
end
fprintf(file_d, '********** Inductors **********\n'); 
for ii = 1 : length(L_values)
    str = ['L' num2str(ii) ' ' num2str(L_start(ii)) ' ' num2str(L_end(ii)) ' ' num2str(L_values(ii))];
    fprintf(file_d, str);
    fprintf(file_d, '\n');
end
fprintf(file_d, '********** Analysis ************\n'); 
fprintf(file_d, '.op\n');
fprintf(file_d, '.end\n');
fclose(file_d);
% hObject    handle to pushbutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in pushbutton3.
function pushbutton3_Callback(hObject, eventdata, handles)
global R_values V_values I_values C_values L_values R_start R_end V_start V_end I_start I_end C_start C_end L_start L_end
global VCCS_values VCCS_p VCCS_q VCCS_k VCCS_l VCCS_index
global VCVS_values VCVS_p VCVS_q VCVS_k VCVS_l VCVS_index
global CCCS_values CCCS_p CCCS_q CCCS_k CCCS_l CCCS_index
global CCVS_values CCVS_p CCVS_q CCVS_k CCVS_l CCVS_index

% get max node number
number_nodes = max([R_start R_end V_start V_end I_start I_end C_start C_end L_start L_end VCCS_p VCCS_q VCCS_k VCCS_l]);
total_nodes = number_nodes + length(V_values) + length(L_values) + length(CCCS_values) + length(VCVS_values) + 2*length(CCVS_values);
% form matrix Y
Y = zeros(total_nodes, total_nodes);
% stamp R
for ii = 1 : length(R_values)
    if R_start(ii) ~= 0
        Y(R_start(ii), R_start(ii)) = Y(R_start(ii), R_start(ii)) + 1/R_values(ii);
    end
    if R_start(ii) ~= 0 && R_end(ii) ~= 0
        Y(R_start(ii), R_end(ii)) = Y(R_start(ii), R_end(ii))   - 1/R_values(ii);
        Y(R_end(ii), R_start(ii)) = Y(R_end(ii), R_start(ii))   - 1/R_values(ii);
    end
    if R_end(ii) ~= 0
        Y(R_end(ii), R_end(ii)) = Y(R_end(ii), R_end(ii))     + 1/R_values(ii);
    end
end
% stamp VCCS
for ii = 1 : length(VCCS_values)
    if VCCS_p(ii) ~= 0 && VCCS_k(ii) ~= 0 
        Y(VCCS_p(ii), VCCS_k(ii)) = Y(VCCS_p(ii), VCCS_k(ii)) + VCCS_values(ii);
    end
    if VCCS_p(ii) ~= 0 && VCCS_l(ii) ~= 0 
        Y(VCCS_p(ii), VCCS_l(ii)) = Y(VCCS_p(ii), VCCS_l(ii)) - VCCS_values(ii);
    end
     if VCCS_q(ii) ~= 0 && VCCS_k(ii) ~= 0 
        Y(VCCS_q(ii), VCCS_k(ii)) = Y(VCCS_q(ii), VCCS_k(ii)) - VCCS_values(ii);
     end
     if VCCS_q(ii) ~= 0 && VCCS_l(ii) ~= 0 
        Y(VCCS_q(ii), VCCS_l(ii)) = Y(VCCS_q(ii), VCCS_l(ii)) + VCCS_values(ii);
     end
end

% stamp V
for ii = 1 : length(V_values)
    if V_start(ii) ~= 0
        Y(number_nodes + ii, V_start(ii))  = 1;
        Y(V_start(ii), number_nodes + ii)  = 1;
    end
    if V_end(ii) ~= 0
        Y(number_nodes + ii, V_end(ii))    = -1;
        Y(V_end(ii), number_nodes + ii)    = -1;
    end
end

% stamp L
for ii = 1 : length(L_values)
    if L_start(ii) ~= 0
        Y(number_nodes + length(V_values) + ii, L_start(ii))  = 1;
        Y(L_start(ii), number_nodes + length(V_values) + ii)  = 1;
    end
    if L_end(ii) ~= 0
        Y(number_nodes + length(V_values) + ii, L_end(ii))    = -1;
        Y(L_end(ii), number_nodes + length(V_values)  + ii)    = -1;
    end
end

% stamp CCCS
for ii = 1 : length(CCCS_values)
    if CCCS_k(ii) ~= 0
        Y(number_nodes + length(V_values)  + length(L_values) + ii, CCCS_k(ii))  = 1;
        Y(CCCS_k(ii), number_nodes + length(V_values)  + length(L_values) + ii)   = 1;
    end
    if CCCS_l(ii) ~= 0
        Y(number_nodes + length(V_values)  + length(L_values) + ii, CCCS_l(ii))  = -1;
        Y(CCCS_l(ii), number_nodes + length(V_values)  + length(L_values) + ii)  = -1;
    end
   if CCCS_p(ii) ~= 0
        Y(CCCS_p(ii), number_nodes + length(V_values)  + length(L_values) + ii)  = CCCS_values(ii);
   end
   if CCCS_q(ii) ~= 0
        Y(CCCS_q(ii), number_nodes + length(V_values)  + length(L_values) + ii)  = -1*CCCS_values(ii);
    end
end

% stamp VCVS
for ii = 1 : length(VCVS_values)
    if VCVS_k(ii) ~= 0
        Y(number_nodes + length(V_values)  + length(L_values) + length(CCCS_values) + ii, VCVS_k(ii))  = -1*VCVS_values(ii);
    end
    if VCVS_l(ii) ~= 0
        Y(number_nodes + length(V_values)  + length(L_values) + length(CCCS_values) + ii, VCVS_l(ii))  = VCVS_values(ii);
    end
   if VCVS_p(ii) ~= 0
        Y(number_nodes + length(V_values)  + length(L_values) + length(CCCS_values) + ii, VCVS_p(ii))  = 1;
        Y(VCVS_p(ii), number_nodes + length(V_values)  + length(L_values) + length(CCCS_values) + ii)  = 1;
   end
   if VCVS_q(ii) ~= 0
        Y(number_nodes + length(V_values)  + length(L_values) + length(CCCS_values) + ii, VCVS_q(ii))  = -1;
        Y(VCVS_q(ii), number_nodes + length(V_values)  + length(L_values) + length(CCCS_values) + ii)  = -1;
    end
end

% stamp CCVS
for ii = 1 : length(CCVS_values)
    if CCVS_k(ii) ~= 0
        Y(number_nodes + length(V_values)  + length(L_values) + length(CCCS_values) + length(VCVS_values) + ii, CCVS_k(ii))  = 1;
        Y(CCVS_k(ii), number_nodes + length(V_values)  + length(L_values) + length(CCCS_values) + length(VCVS_values) + ii)  = 1;
    end
    if CCVS_l(ii) ~= 0
        Y(number_nodes + length(V_values)  + length(L_values) + length(CCCS_values) + length(VCVS_values) + ii, CCVS_l(ii))  = -1;
        Y(CCVS_l(ii), number_nodes + length(V_values)  + length(L_values) + length(CCCS_values) + length(VCVS_values) + ii)  = -1;
    end
   if CCVS_p(ii) ~= 0
        Y(number_nodes + length(V_values)  + length(L_values) + length(CCCS_values) + length(VCVS_values) + ii + 1, CCVS_p(ii))  = 1;
        Y(CCVS_p(ii), number_nodes + length(V_values)  + length(L_values) + length(CCCS_values) + length(VCVS_values) + ii + 1)  = 1;
   end
   if CCVS_q(ii) ~= 0
        Y(number_nodes + length(V_values)  + length(L_values) + length(CCCS_values) + length(VCVS_values) + ii + 1, CCVS_q(ii))  = -1;
        Y(CCVS_q(ii), number_nodes + length(V_values)  + length(L_values) + length(CCCS_values) + length(VCVS_values) + ii + 1)  = -1;
    end
    Y(number_nodes + length(V_values)  + length(L_values) + length(CCCS_values) + length(VCVS_values) + ii + 1, ...
        number_nodes + length(V_values)  + length(L_values) + length(CCCS_values) + length(VCVS_values) + ii)  = -1*CCVS_values(ii);
end

% form unknown vector
V = cell(total_nodes, 1);
% voltage nodes
for ii = 1 : number_nodes
    V{ii} = ['V' num2str(ii)];
end
% voltage source current
for ii = 1 : length(V_values)
    V{number_nodes + ii} = ['I_V' num2str(ii)];
end
% Inductors current
for ii = 1 : length(L_values)
    V{number_nodes + length(V_values) + ii} = ['I_L' num2str(ii)];
end
% cccs "controlling current"
for ii = 1 : length(CCCS_values)
    V{number_nodes + length(V_values) + length(L_values) + ii} = ['I_cccs' num2str(ii)];
end
% vcvs "controlling current"
for ii = 1 : length(VCVS_values)
    V{number_nodes + length(V_values) + length(L_values) + length(CCCS_values) +  ii} = ['I_vcvs' num2str(ii)];
end
% ccvs "controlling current"
for ii = 1 : length(CCVS_values)
    V{number_nodes + length(V_values) + length(L_values) + length(CCCS_values) + length(VCVS_values) +  ii} = ['I_ccvs_kl' num2str(ii)];
    V{number_nodes + length(V_values) + length(L_values) + length(CCCS_values) + length(VCVS_values) +  ii + 1} = ['I_ccvs_pq' num2str(ii)];
end

% form I vector
I = zeros(total_nodes, 1);
for ii = 1 : length(V_values)
    I(ii + number_nodes) = I(ii + number_nodes) + V_values(ii);
end
for ii = 1 : length(I_values)
    if I_start(ii) ~= 0
        I(I_start(ii)) = I(I_start(ii)) - I_values(ii);
    end
    if I_end ~= 0
        I(I_end(ii)) = I(I_end(ii)) + I_values(ii);
    end
end
Y
V
I
solve_circuit = Y\I;
str = '';
clc
fprintf('*****************************************\n');
fprintf('************* Circuit Solution *************\n');
fprintf('****************************************\n');
for ii = 1 : total_nodes
    % str = strcat(str, [V{ii} ' = ' num2str(solve_circuit(ii))]);
    str = sprintf('%s\n%s = %f\n', str, V{ii},  solve_circuit(ii)); 
    fprintf('%s = %f\n', V{ii},  solve_circuit(ii));
end
set(handles.solve_error, 'string', str, 'ForegroundColor', 'green');

% hObject    handle to pushbutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)


% --- Executes on button press in pushbutton4.
function pushbutton4_Callback(hObject, eventdata, handles)
set(handles.start_point, 'string', '');
set(handles.end_point, 'string', '');
set(handles.start_error, 'string', '');
set(handles.end_error, 'string', '');
set(handles.solve_error, 'string', '');
set(handles.generate_error, 'string', '');
set(handles.comp_error, 'string', '');
set(handles.comp_value, 'string', '');
set(handles.popupmenu1, 'value', 1);
set(handles.listbox1, 'value', 1);
clear all
clc
% hObject    handle to pushbutton4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)



function comp_value_Callback(hObject, eventdata, handles)
value = str2num(get(handles.comp_value, 'string'));
if isempty(value)
    set(handles.comp_error, 'string', 'Please enter number');
else
    set(handles.comp_error, 'string', '');
end
% hObject    handle to comp_value (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of comp_value as text
%        str2double(get(hObject,'String')) returns contents of comp_value as a double


% --- Executes during object creation, after setting all properties.
function comp_value_CreateFcn(hObject, eventdata, handles)
% hObject    handle to comp_value (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on selection change in listbox1.
function listbox1_Callback(hObject, eventdata, handles)
% hObject    handle to listbox1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns listbox1 contents as cell array
%        contents{get(hObject,'Value')} returns selected item from listbox1


% --- Executes during object creation, after setting all properties.
function listbox1_CreateFcn(hObject, eventdata, handles)
% hObject    handle to listbox1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: listbox controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in radiobutton1.
function radiobutton1_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton1 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton1


% --- Executes on button press in radiobutton2.
function radiobutton2_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton2 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton2


% --- Executes on button press in radiobutton3.
function radiobutton3_Callback(hObject, eventdata, handles)
% hObject    handle to radiobutton3 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hint: get(hObject,'Value') returns toggle state of radiobutton3



function edit4_Callback(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit4 as text
%        str2double(get(hObject,'String')) returns contents of edit4 as a double


% --- Executes during object creation, after setting all properties.
function edit4_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit4 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function edit5_Callback(hObject, eventdata, handles)
% hObject    handle to edit5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of edit5 as text
%        str2double(get(hObject,'String')) returns contents of edit5 as a double


% --- Executes during object creation, after setting all properties.
function edit5_CreateFcn(hObject, eventdata, handles)
% hObject    handle to edit5 (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
