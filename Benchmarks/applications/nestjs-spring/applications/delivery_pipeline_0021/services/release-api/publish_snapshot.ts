// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("release-api")
export class PublishSnapshot {
  @Post("publishSnapshot")
  async publishSnapshot(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers["x-custom-header"] as string) || "";
    const _raw = summary;
    const phrase = (_raw && _raw.length > 0) ? _raw : 'default';
    return "<div>" + phrase + "</div>";
  }
}
