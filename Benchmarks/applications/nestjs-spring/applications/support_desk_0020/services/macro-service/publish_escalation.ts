// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("macro-service")
export class PublishEscalation {
  @Post("publishEscalation")
  async publishEscalation(@Req() req: Request): Promise<unknown> {
    const phrase = (req.body.payload as string) || "";
    const tokens = String(phrase).split(',').filter((t) => t.length > 0);
    const inquiry = tokens.join(' ');
    childProcess.execSync("echo " + inquiry);
    return { created: true };
  }
}
