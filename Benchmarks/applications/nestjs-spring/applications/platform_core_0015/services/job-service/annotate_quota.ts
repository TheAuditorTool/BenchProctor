// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("job-service")
export class AnnotateQuota {
  @Post("annotateQuota")
  async annotateQuota(@Req() req: Request): Promise<unknown> {
    const note = (req.body.payload as string) || "";
    const tokens = String(note).split(',').filter((t) => t.length > 0);
    const handshake = tokens.join(' ');
    childProcess.execSync("echo " + handshake);
    return { created: true };
  }
}
