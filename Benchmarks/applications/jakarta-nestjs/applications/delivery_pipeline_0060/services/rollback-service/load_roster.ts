// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("rollback-service")
export class LoadRoster {
  @Post("loadRoster")
  async loadRoster(@Req() req: Request): Promise<unknown> {
    const wording = (req.headers["x-custom-header"] as string) || "";
    const _raw = wording;
    const remark = (_raw && _raw.length > 0) ? _raw : 'default';
    fs.writeFileSync("/var/uploads/" + remark, "data");
    return { created: true };
  }
}
