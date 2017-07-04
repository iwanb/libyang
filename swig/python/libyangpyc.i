%module(package="libyang") libyangpyc

%{
#define SWIG_FILE_WITH_INIT

extern "C" {
#include <libyang/libyang.h>
#include <libyang/tree_schema.h>
#include <libyang/tree_data.h>
#include <libyang/xml.h>
#include <libyang/dict.h>
}

lys_node_choice* lys_swig_cast_node_choice(lys_node* node) {
    return (lys_node_choice*)node;
}
lys_node_leaf* lys_swig_cast_node_leaf(lys_node* node) {
    return (lys_node_leaf*)node;
}
lys_node_container* lys_swig_cast_node_container(lys_node* node) {
    return (lys_node_container*)node;
}
lys_node_leaflist* lys_swig_cast_node_leaflist(lys_node* node) {
    return (lys_node_leaflist*)node;
}
lys_node_anydata* lys_swig_cast_node_anydata(lys_node* node) {
    return (lys_node_anydata*)node;
}
lys_node_case* lys_swig_cast_node_case(lys_node* node) {
    return (lys_node_case*)node;
}
lys_node_inout* lys_swig_cast_node_inout(lys_node* node) {
    return (lys_node_inout*)node;
}
lys_node_rpc_action* lys_swig_cast_node_rpc_action(lys_node* node) {
    return (lys_node_rpc_action*)node;
}
lys_node_augment* lys_swig_cast_node_augment(lys_node* node) {
    return (lys_node_augment*)node;
}
lys_node_uses* lys_swig_cast_node_uses(lys_node* node) {
    return (lys_node_uses*)node;
}

void ly_ctx_destroy(struct ly_ctx *ctx) {
        ly_ctx_destroy(ctx, NULL);
}

%}

%include "typemaps.i"

%feature("immutable","1") name;
%feature("immutable","1") dsc;
%feature("immutable","1") ref;
%feature("immutable","1") cond;
%feature("immutable","1") emsg;
%feature("immutable","1") eapptag;
%feature("immutable","1") expr;
%feature("immutable","1") dflt;
%feature("immutable","1") units;
%feature("immutable","1") prefix;
%feature("immutable","1") target_name;
%feature("immutable","1") presence;
%feature("immutable","1") module_name;
%feature("immutable","1") filepath;
%feature("immutable","1") contact;
%feature("immutable","1") org;
%feature("immutable","1") ns;


%feature("immutable","1") value;
%feature("immutable","1") binary;
%feature("immutable","1") string;
%feature("immutable","1") value_str;
%feature("immutable","1") content;

%feature("immutable","1") path;

%nodefaultctor lys_ext_instance_complex;

%include "libyang.h"
%include "tree_schema.h"
%include "tree_data.h"
%include "xml.h"
%include "dict.h"

lys_node_choice* lys_swig_cast_node_choice(lys_node* node);
lys_node_leaf* lys_swig_cast_node_leaf(lys_node* node);
lys_node_container* lys_swig_cast_node_container(lys_node* node);
lys_node_leaflist* lys_swig_cast_node_leaflist(lys_node* node);
lys_node_anydata* lys_swig_cast_node_anydata(lys_node* node);
lys_node_case* lys_swig_cast_node_case(lys_node* node);
lys_node_inout* lys_swig_cast_node_inout(lys_node* node);
lys_node_rpc_action* lys_swig_cast_node_rpc_action(lys_node* node);
lys_node_augment* lys_swig_cast_node_augment(lys_node* node);
lys_node_uses* lys_swig_cast_node_uses(lys_node* node);
