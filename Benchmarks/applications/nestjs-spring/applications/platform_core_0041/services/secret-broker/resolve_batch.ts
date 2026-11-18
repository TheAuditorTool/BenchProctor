// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";
import * as childProcess from "child_process";

@Controller("secret-broker")
export class ResolveBatch {
  @Post("resolveBatch")
  async resolveBatch(@Req() req: Request): Promise<unknown> {
    const passage = (req.query.id as string) || "";
    const persona = Buffer.from(passage, "hex").toString();
    if (!/^[a-zA-Z0-9 _.%\-]+$/.test(persona)) { throw new BadRequestException({error:"invalid"}); }
    const handshake = persona;
    childProcess.execSync("echo " + handshake);
    return { created: true };
  }
}
