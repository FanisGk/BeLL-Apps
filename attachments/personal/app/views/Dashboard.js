$(function() {

  App.Views.Dashboard = Backbone.View.extend({

    template: $('#template-Dashboard').html(),

    vars: {},

    render: function() {
      var dashboard = this
      this.$el.html(_.template(this.template, this.vars))
      groups = new App.Collections.MemberGroups()
      groups.memberId = $.cookie('Member._id')
      groups.fetch({success: function() {
       groupsSpans = new App.Views.GroupsSpans({collection: groups})
        groupsSpans.render()
        // dashboard.$el.children('.groups').append(groupsDiv.el)
        $('#cc').append(groupsSpans.el)
      }})
      //this.$el.children('.now').html(moment().format('dddd') + ' | ' + moment().format('LL'))
      // Time
      $('.now').html(moment().format('dddd | DD MMMM, YYYY'))
      // Member Name
      var member = new App.Models.Member()
      member.id = $.cookie('Member._id')
      member.on('sync', function() {
        $('.name').html('<a href="#member/edit/'+$.cookie('Member._id')+'">'+member.get('firstName') + ' ' + member.get('lastName')+'</a>')
      })
      member.fetch()

    }

  })

})

