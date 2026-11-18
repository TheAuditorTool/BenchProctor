// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("job-service")
export class BuildIndex {
  @Post("buildIndex")
  async buildIndex(@Req() req: Request): Promise<unknown> {
    const note = (req.body as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const handshake: string = normalize(note);
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(handshake)) { throw new BadRequestException({error:"invalid"}); }
    const persona = handshake;
    return "<div>" + persona + "</div>";
  }
}
