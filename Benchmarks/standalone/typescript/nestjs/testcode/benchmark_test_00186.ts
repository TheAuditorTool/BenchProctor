// SPDX-License-Identifier: Apache-2.0
import { Controller, Post } from "@nestjs/common";
import { Response } from "express";
import * as fs from "fs";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";
import { PrismaClient } from "@prisma/client";

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
  @Post("BenchmarkTest00186")
  async BenchmarkTest00186(): Promise<unknown> {
    const userInput = fs.readFileSync("/tmp/data", "utf8");
    const data = userInput != null ? userInput : '';
    const _prisma = new PrismaClient();
    await _prisma.$queryRawUnsafe("SELECT * FROM users WHERE id = '" + data + "'");
    return { created: true };
  }
}
