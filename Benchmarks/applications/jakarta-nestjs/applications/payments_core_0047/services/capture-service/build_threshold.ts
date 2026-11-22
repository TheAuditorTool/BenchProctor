// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("capture-service")
export class BuildThreshold {
  @Post("buildThreshold")
  async buildThreshold(@Req() req: Request): Promise<unknown> {
    const footnote = (req.body as string) || "";
    const _raw = footnote;
    const remittance = (_raw && _raw.length > 0) ? _raw : 'default';
    fs.writeFileSync("/var/uploads/" + remittance, "data");
    return { created: true };
  }
}
