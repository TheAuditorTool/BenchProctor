// SPDX-License-Identifier: Apache-2.0
import { Controller, Param, Post } from "@nestjs/common";
import { Response } from "express";
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
  @Post("BenchmarkTest00345/:id")
  async BenchmarkTest00345(@Param("id") pathId: string): Promise<unknown> {
    const userInput = pathId;
    const data = String(userInput).split(/[ \t]+/).join(" ");
    const recordCount = parseInt(String(data), 10);
    const table = new ArrayBuffer((recordCount * 64) >>> 0);
    return { allocated: table.byteLength };
  }
}
