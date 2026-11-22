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
  @Post("BenchmarkTest00207/:id")
  async BenchmarkTest00207(@Param("id") pathId: string): Promise<unknown> {
    const userInput = pathId;
    const _input = String(userInput);
    let data;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': data = _input.normalize('NFC'); break;
      default: data = _input; break;
    }
    const _coerced = parseFloat(String(data));
    const parsedNum = _coerced;
    new Function("return (" + String(parsedNum) + ");")();
    return { created: true };
  }
}
