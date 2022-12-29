set laststatus=2
set showtabline=2
set clipboard=unnamed
set nu
set tabstop=4
set shiftwidth=4
set smartindent
set autoindent
set background=dark
set backspace=2
set completeopt=menuone,longest
set shortmess+=c
set shell=C:\\WINDOWS\\sysnative\\WindowsPowerShell\\v1.0\\powershell.exe
set cmdheight=1


autocmd GUIEnter * set vb t_vb= " for your GUI
autocmd VimEnter * set vb t_vb=

filetype plugin on
filetype indent on
filetype plugin indent on
syntax on
au FileType perl set filetype=prolog
tmap <S-V> <C-W>"*

map <F11> <Esc>:call libcallnr("gvimfullscreen.dll", "ToggleFullScreen", 0)<CR>
inoremap jk <Esc>
tnoremap jk <C-\><C-n>
nnoremap <Tab> gt
inoremap <expr> <C-j> pumvisible() ? "<C-n>" : "<C-j>"
inoremap <expr> <C-k> pumvisible() ? "<C-p>" : "<C-k>"


call plug#begin("~/vimfiles/plugged")
	Plug 'morhetz/gruvbox'
	Plug 'itchyny/lightline.vim'
	Plug 'vim-scripts/delimitMate.vim'
	Plug 'vim-scripts/AutoComplPop'
	Plug 'adimit/prolog.vim'
	Plug '907th/vim-auto-save'
	Plug 'preservim/nerdtree'
call plug#end()

let g:auto_save = 1
colorscheme gruvbox

if has("gui_running")
  if has("gui_win32")
	set guioptions=Ace 
    set guifont=Consolas:h11:cANSI
	set guioptions -=e
    set guioptions -=m "Hides the menubar
    set guioptions -=T "Hides the toolbar
  endif
endif
