// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("message-api")
export class AnnotateManifest {
  @Post("annotateManifest")
  async annotateManifest(@Req() req: Request): Promise<unknown> {
    const summary = (req.body as string) || "";
    const bulletin = Buffer.from(summary, "base64").toString();
    childProcess.execSync("echo " + bulletin);
    return { created: true };
  }
}
