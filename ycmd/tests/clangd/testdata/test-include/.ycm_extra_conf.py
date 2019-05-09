import os.path


def Settings( **kwargs ):
  filename = kwargs.get( 'filename' )
  if not filename:
    return None
  d = os.path.dirname( kwargs[ 'filename' ] )
  return { 'flags': [ '-iquote', os.path.join( d, 'quote' ),
                      '-I', os.path.join( d, 'system' ),
                      '-iframework', os.path.join( d, 'Frameworks' ),
                      '-nostdinc',
                      '-nostdinc++' ] }
