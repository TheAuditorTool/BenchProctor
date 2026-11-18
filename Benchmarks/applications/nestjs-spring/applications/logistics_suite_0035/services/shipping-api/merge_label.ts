// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("shipping-api")
export class MergeLabel {
  @Post("mergeLabel")
  async mergeLabel(@Req() req: Request): Promise<unknown> {
    const phrase = (req.body as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const parcel: string = normalize(phrase);
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(parcel)) { throw new BadRequestException({error:"invalid"}); }
    const consignment = parcel;
    return "<div>" + consignment + "</div>";
  }
}
