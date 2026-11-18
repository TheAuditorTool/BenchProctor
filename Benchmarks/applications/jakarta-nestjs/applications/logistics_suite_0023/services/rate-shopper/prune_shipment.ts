// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("rate-shopper")
export class PruneShipment {
  @Post("pruneShipment")
  async pruneShipment(@Req() req: Request): Promise<unknown> {
    const caption = (req.body.multipart_field as string) || "";
    const parcel = caption != null ? caption : '';
    JSON.parse(parcel);
    return { created: true };
  }
}
