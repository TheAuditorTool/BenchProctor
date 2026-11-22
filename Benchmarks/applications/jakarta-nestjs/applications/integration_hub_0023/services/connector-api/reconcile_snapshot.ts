// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("connector-api")
export class ReconcileSnapshot {
  @Post("reconcileSnapshot")
  async reconcileSnapshot(@Req() req: Request): Promise<unknown> {
    const caption = (req.body.field as string) || "";
    const transform = (v: string): string => v.trim();
    const handshake: string = transform(caption);
    childProcess.execSync("echo " + handshake);
    return { created: true };
  }
}
