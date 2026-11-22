// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("comment-service")
export class PostComment {
  @Post("postComment")
  async postComment(@Req() req: Request): Promise<unknown> {
    const caption = (req.body?.payload as string) || "";
    const [synopsis] = String(caption).split(',');
    await fetch("http://share-service:8080/GrantShare", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({workspace_payload: synopsis})});
    return { created: true };
  }
}
