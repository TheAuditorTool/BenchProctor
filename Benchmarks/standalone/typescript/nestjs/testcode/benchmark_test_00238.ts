// SPDX-License-Identifier: Apache-2.0
import { Controller, Param, Post } from "@nestjs/common";
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
  @Post("BenchmarkTest00238/:id")
  async BenchmarkTest00238(@Param("id") pathId: string): Promise<unknown> {
    const userInput = pathId;
    const tokens = String(userInput).split(',').filter((t) => t.length > 0);
    const data = tokens.join(' ');
    await db.query("SELECT * FROM users WHERE id = $1", [data]);
    return { created: true };
  }
}
