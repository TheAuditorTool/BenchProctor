// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("sampling-config")
export class CompactManifest {
  @Post("compactManifest")
  async compactManifest(@Req() req: Request): Promise<unknown> {
    const note = (req.body.payload as string) || "";
    const tokens = String(note).split(',').filter((t) => t.length > 0);
    const gauge = tokens.join(' ');
    childProcess.execSync("echo " + gauge);
    return { created: true };
  }
}
