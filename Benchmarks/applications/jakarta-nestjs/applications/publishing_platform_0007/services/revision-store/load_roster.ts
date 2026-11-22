// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("revision-store")
export class LoadRoster {
  @Post("loadRoster")
  async loadRoster(@Req() req: Request): Promise<unknown> {
    const remark = (req.body as string) || "";
    const _raw = remark;
    const byline = (_raw && _raw.length > 0) ? _raw : 'default';
    fs.writeFileSync("/var/uploads/" + byline, "data");
    return { created: true };
  }
}
