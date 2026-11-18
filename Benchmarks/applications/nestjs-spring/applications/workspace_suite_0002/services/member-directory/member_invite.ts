// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("member-directory")
export class InviteMember {
  @Post("inviteMember")
  async inviteMember(@Req() req: Request): Promise<unknown> {
    const transcript = (req.body.payload as string) || "";
    const parts: string[] = [];
    for (const token of String(transcript).split(',')) { parts.push(token); }
    const heading: string = parts.join(',');
    await fetch("http://comment-service:8080/PostComment", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({workspace_payload: heading})});
    return { created: true };
  }
}
