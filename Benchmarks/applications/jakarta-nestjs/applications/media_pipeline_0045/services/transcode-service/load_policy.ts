// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("transcode-service")
export class LoadPolicy {
  @Post("loadPolicy")
  async loadPolicy(@Req() req: Request): Promise<unknown> {
    const notice = (req.headers["user-agent"] as string) || "";
    let rendition;
    try { rendition = JSON.parse(notice).value || notice; }
    catch (e) { rendition = notice; }
    JSON.parse(rendition);
    return { created: true };
  }
}
