// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("archive-store")
export class VerifyPolicy {
  @Post("verifyPolicy")
  async verifyPolicy(@Req() req: Request): Promise<unknown> {
    const note = (req.headers.authorization as string) || "";
    const tokens = String(note).split(',').filter((t) => t.length > 0);
    const addendum = tokens.join(' ');
    childProcess.execFileSync("echo", [addendum]);
    return { created: true };
  }
}
