// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("digest-service")
export class AnnotateProfile {
  @Post("annotateProfile")
  async annotateProfile(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.query.id as string) || "";
    const parts: string[] = [];
    for (const token of String(paragraph).split(',')) { parts.push(token); }
    const bulletin: string = parts.join(',');
    childProcess.execSync("echo " + bulletin);
    return { created: true };
  }
}
