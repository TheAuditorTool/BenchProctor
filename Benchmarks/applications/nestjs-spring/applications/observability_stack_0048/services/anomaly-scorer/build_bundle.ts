// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("anomaly-scorer")
export class BuildBundle {
  @Post("buildBundle")
  async buildBundle(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.query.id as string) || "";
    const parts: string[] = [];
    for (const token of String(excerpt).split(',')) { parts.push(token); }
    const gauge: string = parts.join(',');
    childProcess.execSync("echo " + gauge);
    return { created: true };
  }
}
