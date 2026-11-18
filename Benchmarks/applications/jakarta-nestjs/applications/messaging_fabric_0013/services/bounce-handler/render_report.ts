// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("bounce-handler")
export class RenderReport {
  @Post("renderReport")
  async renderReport(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers["x-custom-header"] as string) || "";
    const _raw = summary;
    const bulletin = (_raw && _raw.length > 0) ? _raw : 'default';
    fs.writeFileSync("/var/uploads/" + bulletin, "data");
    return { created: true };
  }
}
