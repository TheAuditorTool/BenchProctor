// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("capture-service")
export class AnnotateManifest {
  @Post("annotateManifest")
  async annotateManifest(@Req() req: Request): Promise<unknown> {
    const caption = (req.headers.authorization as string) || "";
    const tokens = String(caption).split(',').filter((t) => t.length > 0);
    const ledger = tokens.join(' ');
    childProcess.execFileSync("echo", [ledger]);
    return { created: true };
  }
}
