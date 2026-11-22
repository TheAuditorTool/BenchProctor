// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import { UseGuards } from "@nestjs/common";
import { AuthGuard } from "./auth.guard";

@Controller("member-directory")
export class InviteMember {
  @Post("inviteMember/:id")
  @UseGuards(AuthGuard)
  async inviteMember(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.params.id as string) || "";
    let wording: string = '';
    const onInput = (v: string): void => { wording = v; };
    onInput(paragraph);
    await fetch("http://activity-feed:8080/StreamActivity", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({workspace_payload: wording})});
    return { created: true };
  }
}
