// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as nodeSerialize from "node-serialize";

@Controller("platform-api")
export class AuditThreshold {
  @Post("auditThreshold")
  async auditThreshold(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.body.payload as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(excerpt);
    const handshake: string = readInput();
    nodeSerialize.unserialize(handshake);
    return { created: true };
  }
}
