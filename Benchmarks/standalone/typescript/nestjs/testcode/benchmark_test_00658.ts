// SPDX-License-Identifier: Apache-2.0
import { Controller, Header, Post, BadRequestException } from "@nestjs/common";
import { Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00658")
  @Header("Content-Type", "text/html")
  async BenchmarkTest00658(): Promise<unknown> {
    const userInput = (await db.query("SELECT name FROM users WHERE id = $1", [1])).rows[0].name;
    const data = String(userInput).replace(/\u0000/g, "");
    if (!/^[a-zA-Z0-9 _.#%\-]+$/.test(data)) { throw new BadRequestException({error:"invalid"}); }
    const processed = data;
    return "<div>" + processed + "</div>";
  }
}
