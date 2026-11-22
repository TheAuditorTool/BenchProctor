// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("capture-service")
export class RotateThreshold {
  @Post("rotateThreshold")
  async rotateThreshold(@Req() req: Request): Promise<unknown> {
    const memo = (req.headers.host as string) || "";
    const parts: string[] = [];
    for (const token of String(memo).split(',')) { parts.push(token); }
    const ledger: string = parts.join(',');
    fs.writeFileSync("/var/uploads/" + ledger, "data");
    return { created: true };
  }
}
