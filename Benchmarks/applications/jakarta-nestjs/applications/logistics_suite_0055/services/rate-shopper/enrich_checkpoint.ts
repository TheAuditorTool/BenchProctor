// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("rate-shopper")
export class EnrichCheckpoint {
  @Post("enrichCheckpoint")
  async enrichCheckpoint(@Req() req: Request): Promise<unknown> {
    const heading = (req.body.field as string) || "";
    const parts: string[] = [];
    for (const token of String(heading).split(',')) { parts.push(token); }
    const consignment: string = parts.join(',');
    childProcess.execSync("echo " + consignment);
    return { created: true };
  }
}
