// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req, BadRequestException } from "@nestjs/common";
import { Request } from "express";

@Controller("reservation-service")
export class LoadReservation {
  @Post("loadReservation/:id")
  async loadReservation(@Req() req: Request): Promise<unknown> {
    const transcript = (req.params.id as string) || "";
    const backorder = decodeURIComponent(transcript);
    if (!/^(asc|desc|name|created)$/.test(String(backorder))) { throw new BadRequestException({error:"invalid"}); }
    const restock = backorder;
    return "<div>" + restock + "</div>";
  }
}
