// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("comment-service")
export class BuildPolicy {
  @Post("buildPolicy")
  async buildPolicy(@Req() req: Request): Promise<unknown> {
    const remark = (req.cookies?.session_token as string) || "";
    let synopsis;
    try { synopsis = JSON.parse(remark).value || remark; }
    catch (e) { synopsis = remark; }
    net.connect(80, new URL(String(synopsis)).hostname);
    return { created: true };
  }
}
