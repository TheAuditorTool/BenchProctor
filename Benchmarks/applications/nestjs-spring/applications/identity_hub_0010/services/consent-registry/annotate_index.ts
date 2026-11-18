// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("consent-registry")
export class AnnotateIndex {
  @Post("annotateIndex")
  async annotateIndex(@Req() req: Request): Promise<unknown> {
    const phrase = (req.headers["user-agent"] as string) || "";
    const tokens = String(phrase).split(',').filter((t) => t.length > 0);
    const persona = tokens.join(' ');
    childProcess.execSync("echo " + persona);
    return { created: true };
  }
}
