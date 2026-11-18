// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("comment-service")
export class PostComment {
  @Post("postComment")
  async postComment(@Req() req: Request): Promise<unknown> {
    const remark = (req.body as string) || "";
    const transform = (v: string): string => v.trim();
    const synopsis: string = transform(remark);
    await fetch("http://presence-hub:8080/TrackPresence", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({workspace_payload: synopsis})});
    return { created: true };
  }
}
