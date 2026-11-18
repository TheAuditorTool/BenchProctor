// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("platform-api")
export class AnnotateProfile {
  @Post("annotateProfile")
  async annotateProfile(@Req() req: Request): Promise<unknown> {
    const note = (req.query.id as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(note);
    const handshake: string = readInput();
    JSON.parse(handshake);
    return { created: true };
  }
}
