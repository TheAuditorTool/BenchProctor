// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("registry-service")
export class PublishSnapshot {
  @Post("publishSnapshot")
  async publishSnapshot(@Req() req: Request): Promise<unknown> {
    const heading = (req.body?.payload as string) || "";
    const handshake = heading != null ? heading : '';
    childProcess.execSync("echo " + handshake);
    return { created: true };
  }
}
