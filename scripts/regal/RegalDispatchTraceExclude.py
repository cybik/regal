# we need to exclude these functions from the dispatch becuse they do not exist in apitrace
exclude = [

  'glMatrixIndexPointerOES',
  'glWeightPointerOES',

  'glXBindTexImageATI',
  'glXBlitContextFramebufferAMD',
  'glXChooseFBConfigSGIX',
  'glXCreateAssociatedContextAMD',
  'glXCreateAssociatedContextAttribsAMD',
  'glXDeleteAssociatedContextAMD',
  'glXDrawableAttribATI',
  'glXGetContextGPUIDAMD',
  'glXGetCurrentAssociatedContextAMD',
  'glXGetGPUIDsAMD',
  'glXGetGPUInfoAMD',
  'glXGetTransparentIndexSUN',
  'glXGetVideoResizeSUN',
  'glXMakeAssociatedContextCurrentAMD',
  'glXReleaseTexImageATI',
  'glXVideoResizeSUN',

  'wglChoosePixelFormatARB',
  'wglEnumGpuDevicesNV',
  'wglGetDefaultProcAddress',
  'wglGetPixelFormatAttribfvARB',
  'wglGetPixelFormatAttribfvEXT',
  'wglGetPixelFormatAttribivARB',
  'wglGetPixelFormatAttribivEXT',
  'wglGetProcAddress',

  'EGL_KHR_stream_consumer_gltexture',
  'EGL_KHR_stream_cross_process_fd',
  'EGL_KHR_stream_producer_eglsurface',
  'EGL_KHR_wait_sync',
  'EGL_NV_coverage_sample',

  'GL_AMD_interleaved_elements',
  'GL_AMD_stencil_operation_extended',

  'GL_ANGLE_instanced_arrays',
  'GL_ANGLE_timer_query',
  'GL_ANGLE_translated_shader_source',

  'GL_APPLE_copy_texture_levels',
  'GL_APPLE_sync',

  'GL_ARB_bindless_texture',
  'GL_ARB_cl_event',
  'GL_ARB_compute_variable_group_size',
  'GL_ARB_indirect_parameters',
  'GL_ARB_sparse_texture',

  'GL_EXT_disjoint_timer_query',
  'GL_EXT_fragment_lighting',
  'GL_EXT_map_buffer_range',
  'GL_EXT_multisampled_render_to_texture',
  'GL_EXT_multiview_draw_buffers',
  'GL_EXT_robustness',
  'GL_EXT_scene_marker',
  'GL_EXT_texture_storage',

  'GL_INTEL_map_texture',
  'GL_INTEL_texture_scissor',

  'GL_NV_blend_equation_advanced',
  'GL_NV_blend_equation_advanced_coherent',
  'GL_NV_copy_buffer',
  'GL_NV_non_square_matrices',
  'GL_NV_vdpau_interop',

  'GL_OES_single_precision',

  'GL_QCOM_alpha_test',
  'GL_QCOM_driver_control',
  'GL_QCOM_extended_get',
  'GL_QCOM_extended_get2',
  'GL_QCOM_tiled_rendering',

  'GL_REGAL_log',

  'GL_SGIX_fog_texture',

  'GL_SUN_read_video_pixels',
]
