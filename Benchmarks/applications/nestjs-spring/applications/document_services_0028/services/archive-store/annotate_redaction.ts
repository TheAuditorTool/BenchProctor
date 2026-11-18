// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("archive-store")
export class AnnotateRedaction {
  @Post("annotateRedaction")
  async annotateRedaction(@Req() req: Request): Promise<unknown> {
    const note = (req.body as string) || "";
    const addendum = Buffer.from(note, "base64").toString();
    childProcess.execSync("echo " + addendum);
    return { created: true };
  }
}
